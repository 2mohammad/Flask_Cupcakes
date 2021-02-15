async function getFromFlask(x){
    const response = await axios({
        method: x,
        url: '/api/cupcakes'
    })
    return response
}

async function printr(){
        const x = 'get'
        const result = await getFromFlask(x)
        console.log(result.data.cupcakes[0])
        const list = $(`<ul></ul>`)
        for (let i =0; i < result.data.cupcakes.length; i++){
            let item = $(`<li>${result.data.cupcakes[i].flavor}</li>`)
            list.append(item)
        }
        $('body').append(list)
}


function submit(){
    const submitbtn = document.getElementById("add_cupcake")
    submitbtn.addEventListener("click", ()=>{
        const cupcake = {
        flavor : document.getElementById("flavor").value,
        size : document.getElementById("size").value,
        image : document.getElementById("image").value,
        rating : document.getElementById("rating").value
        }
        console.log(cupcake)
        axios.post('/api/cupcakes', cupcake)
    })

}


submit()
printr()