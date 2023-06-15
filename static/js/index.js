const greenBlocks = document.querySelectorAll('.green')
const yellowBlocks = document.querySelectorAll('.yellow')

function isLetter(str){
    const isUpppercase = (char) => 'A' <= char && char <= 'Z';
    const isLowerCase = (char) => 'a' <= char && char <= 'z';
    return str.length === 1 && (isLowerCase(str[0])|| isUpppercase(str[0]))
}

greenBlocks.forEach(input=> input.onkeydown = (e) =>{
    let key = e.key
    const currInput = parseInt(input.id.replace('green', ''))
    if(key == 'Delete' || key == 'Backspace'){
        if(currInput > 0){
            input.value = '';
            e.preventDefault()
            greenBlocks[currInput-1].focus()
        }
    }
    else if(isLetter(key)) {
        e.preventDefault()
        if(currInput < greenBlocks.length-1){
            input.value = key.toUpperCase()
            greenBlocks[currInput+1].focus()
        }
        else{
            input.value = key.toUpperCase()
        }
    }
})

yellowBlocks.forEach(input=> input.onkeydown = (e) =>{
    let key = e.key
    const currInput = parseInt(input.id.replace('yellow', ''))
    if(key == 'Delete' || key == 'Backspace'){
        if(currInput > 0){
            input.value = '';
            e.preventDefault()
            yellowBlocks[currInput-1].focus()
        }
    }
    else if(isLetter(key)) {
        e.preventDefault()
        if(currInput < yellowBlocks.length-1){
            input.value = key.toUpperCase()
            yellowBlocks[currInput+1].focus()
        }
        else{
            input.value = key.toUpperCase()
        }
    }
})

document.querySelector('#solveBtn').onclick = (event) =>{
    green = greenBlocks.map(input => input.value)
    
}