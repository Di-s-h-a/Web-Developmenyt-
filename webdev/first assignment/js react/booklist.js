function book({ book }){
    return(
        <div>
            <Thumbnail book = {book} />
            <a href = 'book.url'>
                <h3>{book.title}</h3>
                <p>{book.description}</p>
            </a>
            <LikeButton book = {book}></LikeButton>
        </div>
);
}
function bookList({ videos, emptyHeading}){
    const count = book.length;
    let heading = emptyheading;
    if (count>0){
        const noun = count>1?'Boooks':'Book';
        heading = count + '' + noun;
    }
    return(
        <section>
            <h2>{heading}</h2>
            {
                book.map(book=>
                    <book key ={book.id} book = {book}/>
                )
            }
        </section>
    );
}