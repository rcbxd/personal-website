const converter = new showdown.Converter();
const newHTML = converter.makeHtml(document.getElementById("post_body_text").value)
document.getElementById("post_body").innerHTML = newHTML;
const body_titles = Array.from(document.getElementById("post_body").childNodes).filter(t => t.localName === "h1");
body_titles.forEach(t => {
    t.outerHTML = `<h1 class="link-title"><a href="#${t.innerHTML.toLowerCase().split(" ").join("")}"><i class="fas fa-link"></i></a > ${t.innerHTML}</h1>`;
})