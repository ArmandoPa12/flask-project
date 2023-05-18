let displayValue = "";

function addDisplay(value) {
    displayValue += value;
    document.getElementById("result").value = displayValue;
}

function clearDisplay() {
    displayValue = ""
    document.getElementById("result").value = "";
    document.getElementById("dato").value = "";
}

function send() {
    document.getElementById("dato").value = displayValue;
    // document.getElementById("dato").textContent = displayValue;
}