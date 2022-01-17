const rowElems = $(".row")
const btnCancelElem = $("form .btn-cancel")
const btnDoneElem = $("form .btn-done")
const btnJoinElem = $("form .btn-join")
const popupContainer = $(".popup-container")
const nameElem = $("form input[type='text']")
const linkElem = $("form input[type='url']")
const caretElem = $(".caret")
let currRow;

function getTime(t) {
    time = `${(t - 1) % 12 + 1} ${t < 12 ? 'AM' : 'PM'}`
    return time.length != 5 ? '0' + time : time
}

for (let i = 0; i < 12; i++) {
    rowElems.eq(i).attr("data-time", getTime(9 + i))
}

document.onload = function () {
    document.getElementById('current_row').value = ""
}

rowElems.click(function () {
    currRow = $(this)
    currRow_id = currRow.attr("id")
    document.getElementById('current_row').value = currRow_id
    task = document.getElementById(currRow_id).innerHTML
    url = document.getElementById(currRow_id).className.split(" ")[1]
    document.getElementById('task').value = task
    document.getElementById('link').value = url
    checkBtnStateinrow()
    popupContainer.fadeIn("fastest")
    popupContainer.css("display", "grid")
});

function checkBtnStateinrow() {
    const name = nameElem.val()
    const link = linkElem.val()
    if (name == '' && link != '') btnDoneElem.attr("disabled", "disabled")
    else btnDoneElem.removeAttr("disabled")
    if (link == '') btnJoinElem.attr("disabled", "disabled")
    else btnJoinElem.removeAttr("disabled")
}

function checkBtnState() {
    const name = nameElem.val()
    const link = linkElem.val()
    if (name == '' && link != '') btnDoneElem.attr("disabled", "disabled")
    else btnDoneElem.removeAttr("disabled")
}

nameElem.on("input", checkBtnState)
linkElem.on("input", checkBtnState)

btnCancelElem.click(() => {
    popupContainer.fadeOut("fastest")
})

btnDoneElem.click(() => {
    popupContainer.fadeOut("fastest")
})

btnJoinElem.click(() => {
    popupContainer.fadeOut("fastest")
    if (currRow_id == '9-10') {
        url = document.getElementById('9-10').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '10-11') {
        url = document.getElementById('10-11').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '11-12') {
        url = document.getElementById('11-12').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '12-13') {
        url = document.getElementById('12-13').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '13-14') {
        url = document.getElementById('13-14').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '14-15') {
        url = document.getElementById('14-15').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '15-16') {
        url = document.getElementById('15-16').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '16-17') {
        url = document.getElementById('16-17').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '17-18') {
        url = document.getElementById('17-18').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '18-19') {
        url = document.getElementById('18-19').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '19-20') {
        url = document.getElementById('19-20').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
    else if (currRow_id == '20-21') {
        url = document.getElementById('20-21').className.split(" ")[1]
        window.open(url, '_blank').focus();
    }
})

function moveCaret() {
    const d = new Date()
    const hours = d.getHours()
    const minutes = d.getMinutes()
    const elapsedPercent = (hours - 9 + minutes / 60) / 12 * 100
    caretElem.css("top", `${Math.min(100, elapsedPercent)}%`)
}

moveCaretInterval = setInterval(moveCaret(), 60 * 1000)