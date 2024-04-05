const fs = require('fs')

fs.readFile('number_one.txt', 'utf8', (err, data) => {
    if(err){
        console.log('파일을 읽는 도중 오류가 발생하였습니다.', err)
        return;
    }
    console.log('파일 내용:', data)
})

let content = 'four'
fs.writeFile('number_four.txt', content, (err) => {
    if(err){
        console.log('파일을 쓰는 도중 오류가 발생했습니다.', err)
        return;
    }
    console.log('파일 쓰기가 완료되었습니다.')    
})

content = 'It is very difficult thing, right?'
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('파일을 쓰는 도중 오류가 발생했습니다.', err)
        return;
    }
    console.log('파일 생성 및 쓰기가 완료되었습니다.')    
})

content = ' But your skill will be growning.'
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('파일을 쓰는 도중 오류가 발생했습니다.', err)
        return;
    }
    console.log('파일 생성 및 쓰기가 완료되었습니다.')    
})