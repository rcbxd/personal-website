const converter = new showdown.Converter();
const newHTML = converter.makeHtml(document.getElementById("post_body_text").value)

document.getElementById("post_body").innerHTML = newHTML;

const body_titles = Array.from(document.getElementById("post_body").childNodes).filter(t => t.localName === "h1");
body_titles.forEach(t => {
    t.outerHTML = `<h1 class="link-title"><a href="#${t.innerHTML.toLowerCase().split(" ").join("")}"><i class="fas fa-link"></i></a > ${t.innerHTML}</h1>`;
})

const images = Array.from(document.getElementsByClassName("post_body_image"))
const document_body = document.getElementById("post_body");
let i = 0;
while (document_body.innerHTML.indexOf("{{img") !== -1) {
    let oldHTML = document_body.innerHTML;
    oldHTML = document_body.innerHTML.substring(0, document_body.innerHTML.indexOf("{{img"));
    oldHTML += `<img src=${images[i].value} class="post_body_image">`
    oldHTML += document_body.innerHTML.substring(document_body.innerHTML.indexOf("{{img") + 9);
    document_body.innerHTML = oldHTML;
    i++;
}