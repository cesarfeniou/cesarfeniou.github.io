<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>César Feniou</title>
  <meta name="description" content="Quantum Research Scientist" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="wrap">
    <nav class="nav">
      <a class="brand" href="/">César Feniou</a>
      <div class="links">
        <a href="#publications">Publications</a>
        <a href="#news">News</a>
        <a href="/cv.pdf">CV</a>
      </div>
    </nav>
  </header>

  <main class="wrap">
    <section class="hero">
      <h1>Quantum Research Scientist</h1>
      <p>
        Short bio here. One or two sentences about your research interests.
      </p>
      <div class="cta">
        <a class="btn" href="mailto:your@email.com">Email</a>
        <a class="btn ghost" href="https://github.com/chemcesar">GitHub</a>
      </div>
    </section>

    <section id="publications" class="section">
      <h2>Publications</h2>
      <ul class="list">
        <li>
          <span class="title">Paper title</span>
          <span class="meta">Authors · Venue · Year</span>
          <span class="actions">
            <a href="#">PDF</a> · <a href="#">arXiv</a> · <a href="#">Code</a>
          </span>
        </li>
      </ul>
    </section>

    <section id="news" class="section">
      <h2>News</h2>
      <ul class="list">
        <li><span class="meta">2026-01-29</span> Started a new project on …</li>
      </ul>
    </section>
  </main>

  <footer class="wrap footer">
    <span>© <span id="y"></span> César Feniou</span>
  </footer>

  <script>
    document.getElementById("y").textContent = new Date().getFullYear();
  </script>
</body>
</html>
