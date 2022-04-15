function btnCalculate1() {
    var bgBody = document.getElementById("body");        
    bgBody.style.backgroundColor = "#FFFF99";    
    tickets = parseInt(prompt("Type tickets"));
    souvenirs = parseInt(prompt("Type souvenirs"));
    eat = parseInt(prompt("Type eat"));
    expences = tickets + eat + souvenirs;
    alert("your expenses are: " + expences);    
}


function btnCalculate2() {
    var bgBody = document.getElementById("body");
    bgBody.style.backgroundColor = "#99FF66";    
    expences = parseInt(prompt("Type your expences"));
    salary = parseInt(prompt("Type your salary"));
    savings = parseInt(prompt("Type your savaings"));
    budget = (salary + savings) - expences;
    alert("your travel budget is: " + budget);
}


function btnCheck() {    
    var bgBody = document.getElementById("body");
    bgBody.style.backgroundColor = "#9966FF";        
    number = prompt("Type number")
    if (number % 2 == 0){
        alert("The number " + number + " is even ");
    }else{
        alert("The number " + number + " is odd ");
    }
}