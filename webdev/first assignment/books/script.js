class Book{
    constructor(title,author,category){
        this.title = title;
        this.author = author;
        this.category = category;
    }
}
let btn = socument.getElementById("submit");
let books = []
function submitForm(event){
    event.preventDefault();
    let title = document.getElementById('title').ariaValueText;
    let author = document.getElementById('author').value;
    let category = document.getElementById('category').value;
}
let book =new Book(title,author,category);
books.push(book);
let elementUL = document.createElement('ul');
function addElemet(){
    let elementTitle = document.createElement('li');
    let elementAuthor = document.createElement('li');
    let elementCategory = document.createElement('li');

    let titleContent = document.createTextNode("Title: " + books[0].title);
    let authorContent = document.createTextNode("Author: " + books[0].author);
    let categoryContent = document.createTextNode("Category: " + books[0].category);

    elementUL.appendChild(elementTitle);
    elementUL.appendChild(elementAuthor);
    elementUL.appendChild(elementCategory);

    document.querySelector('body').appendChild(elementUL);
}
addElemet()
btn,addEventListener('click',submitForm)