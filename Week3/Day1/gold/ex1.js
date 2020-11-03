
    let table = document.body.firstElementChild;
    let allBooks = [{
        Title: "Harry Potter",
        Author: "J.K Rowling",
        img: "https://images-na.ssl-images-amazon.com/images/I/815v2OuIHXL._AC_SL1500_.jpg",
        alreadyRead: false
    },
    {   Title: "Legacy of Ashes",
        Author: "Tim Wiener",
        img: "https://images-na.ssl-images-amazon.com/images/I/81QBEaG64PL.jpg",
        alreadyRead: true}
    ]

    let div = document.createElement("div");
    div.setAttribute("id", "tbl");
    div.style.marginTop = "50px";
    document.body.appendChild(div);

    document.getElementById("tbl").innerHTML = "<table border = '1'>" +
    "<thead>"+"<tr>" + "<th>Title</th>" + "<th>Author</th>" + "<th>Image</th>" + "<th>Read?</th>" + "</tr>"+ "</thead>"
    + "<tbody>" + "</tbody>";

    let tableBody = document.querySelector("tbody");
    let isRead = "";
    let a = "<tbody>";

    for(i = 0; i<allBooks.length; i++){
        let read = allBooks[i].alreadyRead;

        if(read===true){
            isRead = "Yes";
        }
        else{
            isRead = "No";
        }

        a = a + "<tr>";
        a = a + "<td>" + allBooks[i].Title + "</td>";
        a = a + "<td>" + allBooks[i].Author + "</td>";
        a = a + "<td>" + '<img width = 100 src = "'+allBooks[i].img + '">' + "</td>";
        a = a + "<td>" + isRead + "</td>";
        a = a + "</tr>";
        

    }
    a = a + "</tbody>"
    tableBody.innerHTML = a;

    let tableData = document.querySelectorAll("td");
    
    for(j = 0; j<tableData.length; j++){

        if(tableData[j].innerHTML==="Yes"){
            tableData[j].style.color = "red";
        }
    }



