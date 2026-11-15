/* Pythonずかん: 検索、たどってきた道、ホバープレビュー、コピーボタン */
(function () {
  var D = (window.ZUKAN && window.ZUKAN.pages) || {};
  var body = document.body;

  function hrefOf(slug) { return slug + ".html"; }

  /* ---- コピーボタン ---- */
  Array.prototype.forEach.call(document.querySelectorAll(".copy"), function (b) {
    b.addEventListener("click", function () {
      var pre = b.closest(".runbox").querySelector(".code pre");
      var text = pre.innerText.replace(/\n$/, "");
      function done(ok) {
        b.textContent = ok ? "コピーしました" : "選んでコピーしてね";
        setTimeout(function () { b.textContent = "コピー"; }, 1600);
      }
      function fallback() {
        try {
          var r = document.createRange();
          r.selectNodeContents(pre);
          var s = window.getSelection();
          s.removeAllRanges();
          s.addRange(r);
        } catch (e) {}
        done(false);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, fallback);
      } else {
        fallback();
      }
    });
  });

  /* ---- たどってきた道 ---- */
  (function () {
    var box = document.getElementById("trail");
    var cur = { s: body.getAttribute("data-slug"), t: body.getAttribute("data-title") };
    var key = "zukan-trail";
    var trail = [];
    try { trail = JSON.parse(sessionStorage.getItem(key) || "[]"); } catch (e) { trail = []; }
    if (!Array.isArray(trail)) trail = [];
    if (cur.s === "index") {
      trail = [cur];
    } else {
      var i = -1;
      trail.forEach(function (x, k) { if (x.s === cur.s) i = k; });
      if (i >= 0) trail = trail.slice(0, i + 1); else trail.push(cur);
      if (trail.length > 6) trail = trail.slice(-6);
    }
    try { sessionStorage.setItem(key, JSON.stringify(trail)); } catch (e) {}
    if (!box || trail.length < 2) return;
    var html = '<span class="lbl">たどってきた道</span>';
    trail.forEach(function (x, k) {
      var last = k === trail.length - 1;
      var title = x.t || x.s;
      if (k > 0) html += "<span>›</span>";
      if (last) {
        html += '<span class="now"></span>';
      } else {
        html += '<a href="' + hrefOf(x.s) + '"></a>';
      }
    });
    box.innerHTML = html;
    var nodes = box.querySelectorAll("a, .now");
    trail.forEach(function (x, k) { nodes[k].textContent = x.t || x.s; });
    box.hidden = false;
  })();

  /* ---- 検索 ---- */
  (function () {
    var q = document.getElementById("q");
    var res = document.getElementById("results");
    if (!q || !res) return;
    var items = Object.keys(D).map(function (s) {
      return { s: s, t: D[s][0], d: D[s][1], a: (D[s][3] || "") };
    });
    function norm(x) { return (x || "").toLowerCase(); }
    var sel = -1;
    function render() {
      var v = norm(q.value.trim());
      if (!v) { res.hidden = true; res.innerHTML = ""; return; }
      var hits = items.filter(function (it) {
        return norm(it.t + " " + it.a + " " + it.d).indexOf(v) >= 0;
      });
      hits.sort(function (a, b) {
        var as = norm(a.t).indexOf(v) === 0 || norm(a.a).indexOf(v) === 0 ? 0 : 1;
        var bs = norm(b.t).indexOf(v) === 0 || norm(b.a).indexOf(v) === 0 ? 0 : 1;
        return as - bs;
      });
      hits = hits.slice(0, 8);
      sel = hits.length ? 0 : -1;
      if (!hits.length) {
        res.innerHTML = '<li><a style="pointer-events:none">見つかりませんでした</a></li>';
        res.hidden = false;
        return;
      }
      res.innerHTML = hits.map(function (it, k) {
        return '<li><a href="' + hrefOf(it.s) + '"' + (k === 0 ? ' class="on"' : "") + "></a></li>";
      }).join("");
      Array.prototype.forEach.call(res.querySelectorAll("a"), function (a, k) {
        var t = document.createElement("span");
        t.textContent = hits[k].t;
        var d = document.createElement("small");
        d.textContent = hits[k].d;
        a.appendChild(t);
        a.appendChild(d);
      });
      res.hidden = false;
    }
    function move(dir) {
      var as = res.querySelectorAll("a");
      if (!as.length || res.hidden) return;
      if (sel >= 0) as[sel].classList.remove("on");
      sel = (sel + dir + as.length) % as.length;
      as[sel].classList.add("on");
    }
    q.addEventListener("input", render);
    q.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
      else if (e.key === "Escape") { res.hidden = true; }
      else if (e.key === "Enter") {
        var as = res.querySelectorAll("a");
        if (!res.hidden && sel >= 0 && as[sel] && as[sel].getAttribute("href")) {
          window.location.href = as[sel].getAttribute("href");
        }
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search")) res.hidden = true;
    });
  })();

  /* ---- ホバーでプレビュー（マウスがある端末だけ） ---- */
  (function () {
    if (!window.matchMedia || !window.matchMedia("(hover: hover)").matches) return;
    var CH = { 0: "第0章 はじめる前に", 1: "第1章 計算処理", 2: "第2章 変数とリスト",
               3: "第3章 繰り返し", 4: "第4章 条件分岐", 5: "第5章 関数", 6: "第6章 モジュール",
               7: "第7章 Pyxelで作ろう", 8: "第8章 Pyxel辞典", 9: "第9章 道具と困ったとき" };
    var card = document.createElement("div");
    card.className = "peek";
    card.hidden = true;
    card.setAttribute("role", "tooltip");
    document.body.appendChild(card);
    var showT = null, hideT = null;

    function show(a) {
      var slug = a.getAttribute("data-slug");
      var d = D[slug];
      if (!d) return;
      card.className = "peek" + (d[2] !== "" ? " ch-" + d[2] : "");
      card.innerHTML = '<div class="pk-ch"></div><p class="pk-t"></p><p class="pk-s"></p>';
      card.querySelector(".pk-ch").textContent = d[2] !== "" ? CH[d[2]] : "";
      card.querySelector(".pk-t").textContent = d[0];
      card.querySelector(".pk-s").textContent = d[1];
      card.hidden = false;
      var r = a.getBoundingClientRect();
      var w = card.offsetWidth;
      var left = Math.max(8, Math.min(r.left + window.pageXOffset, window.pageXOffset + document.documentElement.clientWidth - w - 8));
      card.style.left = left + "px";
      card.style.top = (r.bottom + window.pageYOffset + 6) + "px";
    }
    function hide() { card.hidden = true; }

    document.addEventListener("mouseover", function (e) {
      var a = e.target.closest && e.target.closest("a[data-slug]");
      if (a) {
        clearTimeout(hideT);
        clearTimeout(showT);
        showT = setTimeout(function () { show(a); }, 300);
      } else if (e.target.closest && e.target.closest(".peek")) {
        clearTimeout(hideT);
      }
    });
    document.addEventListener("mouseout", function (e) {
      var t = e.target.closest && (e.target.closest("a[data-slug]") || e.target.closest(".peek"));
      if (t) {
        clearTimeout(showT);
        hideT = setTimeout(hide, 180);
      }
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(); });
  })();
})();
