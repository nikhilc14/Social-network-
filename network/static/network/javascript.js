document.addEventListener('DOMContentLoaded',function(){
const icons = document.getElementsByClassName('fa-solid fa-heart');
for (let i = 0; i < icons.length ; i++){
    let n = true 
    fetch(`/likes/${icons[i].parentElement.children[1].innerHTML}`)
    .then(response => response.json())
    .then(response => { 
        n = response["clicking"];
        n_click(n);
    })
    .catch(error=>{
      console.log('Error:',error);
    });

    function n_click(n){
        if (n==true){
            icons[i].style.color = 'red';
        }
        else {
            icons[i].style.color = 'gray';
        }
    }

}})
document.addEventListener('DOMContentLoaded',function(){
            document.addEventListener('click', event => {
                const element =  event.target;

                if (element.className === 'fa-solid fa-heart'){

                        //getting the exisiting items of html 
                        user = element.parentNode.children[0].innerHTML;
                        post = element.parentNode.children[1].innerHTML;
                        likes = element.parentNode.children[4].innerHTML;

                        //Get likes which are already there 
                        fetch(`/likes/${post}`)
                        .then(response => response.json())
                        .then(response => { 
                            clicked = response["clicking"];
                            like_click(clicked);
                            console.log("Harshita")
                        })
                        .catch(error=>{
                          console.log('Error:',error);
                        });


                       
                    async function like_click(clicked){
                        
                        //if user clicks on the element
                        if (clicked === true){
                            change = element.parentNode.children[4];
                            //animation 
                            element.style.color = 'gray';
                            element.style.animationDirection = 'reverse';
                            element.style.animationPlayState = 'running';
                            element.addEventListener('animationend',function(){
                                element.style.animationPlayState = 'paused';

                            })


                            //Posting 
                            fetch(`/likes/${post}`,{
                                method:"POST",
                                body:JSON.stringify({
                                    likes:likes,
                                    clicked:false
                                })
                            })
                            .then(response => response.text())
                            .then(response => {
                                console.log("Posted 1");
                            })
                            .catch(error=>{
                            console.log('Error:',error);
                            });

                            change.innerHTML = parseInt(change.innerHTML) - 1 ;


                            //replacing the node 
                            var newone = element.cloneNode(true);
                            element.parentNode.replaceChild(newone, element);
                        }
                        else {
                            change = element.parentNode.children[4];
                            //animation 
                            element.style.animationDirection = 'normal';
                            element.style.animationPlayState = 'running';
                            element.addEventListener('animationend',function(){
                                element.style.animationPlayState = 'paused';
                            })

                            //Posting 
                            fetch(`/likes/${post}`,{
                                method:"POST",
                                body:JSON.stringify({
                                    likes:likes,
                                    clicked:true
                                })
                            })
                            .then(response => response.text())
                            .then(response => {
                                console.log("Posted 2 ");
                            })
                            .catch(error=>{
                            console.log('Error:',error);
                            });

                            //likes
                            change.innerHTML = parseInt(change.innerHTML) + 1 ;

                            //replacing the node
                            var newone = element.cloneNode(true);
                            element.parentNode.replaceChild(newone, element);

                        }
                }
                }
            })
        })
        i=0
        let dt
        let user_post
        let temp
        document.addEventListener('DOMContentLoaded',function(){

            fetch('/user_request')
            .then(response => response.json())
            .then(data => {
                document.querySelectorAll('.post_info').forEach(post => show_edit(post,data));
                dt = data 
            })
            
            function show_edit(post,data){
                console.log(data)
                console.log(post.innerHTML)
                if(post.innerHTML==data["user"]){
                    const element2 = document.createElement('div');
                    element2.className = 'btn btn-link editing';
                    element2.innerHTML = "Edit";
                    
                    post.parentElement.append(element2)
                    }
            }
            
            document.addEventListener('click',function(){
                const element = event.target;
                if (element.className === 'btn btn-link editing'){
                    temp = element.parentNode.innerHTML 
                    user_post = element.parentNode.children[1].innerHTML
                    timestamp = element.parentNode.children[2].innerHTML 
                    counted = element.parentNode.children[4].innerHTML
                    element.parentNode.innerHTML = '<textarea class="edit_textarea"  maxlength="5000" cols="90" rows="3" class="text_area"> </textarea>'+
                    '<button type="submit" class="btn btn-primary edit_submit">Save</button>';
                    }

                if (element.className === 'btn btn-primary edit_submit' ){
                    const text_value = document.querySelector(".edit_textarea").value;
                    fetch('/edit',{
                        method:"POST",
                        body:JSON.stringify({
                            post:text_value,
                            user:dt["user"],
                            index:user_post

                        })
                    })
                    .then(response => response.text())
                    .then(result => {
                        // Print result
                        console.log(result);
                    })
                    .catch(error=>{
                    console.log('Error:',error);
                    });

                    const new_user = document.createElement('a')
                    const new_div = document.createElement('div')
                    const new_timestamp = document.createElement('p')
                    const new_icon = document.createElement('i')
                    const the_like_count = document.createElement('b')

                    new_user.className = 'post_info';
                    new_div.className = 'post_post';
                    the_like_count.className = 'like_count';
                    new_user.href = `/profile/${dt["user"]}`


                    new_user.innerHTML = dt["user"]
                    new_div.innerHTML = text_value 
                    new_timestamp.innerHTML  = timestamp
                    new_timestamp.className = 'timestamp';
                    new_icon.className = "fa-solid fa-heart";
                    new_icon.style.color = 'gray';
                    the_like_count.innerHTML = counted;
                    


                    element.parentNode.append(new_user);
                    element.parentElement.append(new_div);
                    element.parentNode.append(new_timestamp);
                    element.parentNode.append(new_icon);
                    element.parentNode.append(the_like_count);


                    element.parentElement.removeChild(element.parentElement.children[0]);
                    element.parentElement.removeChild(element.parentElement.children[0]);

                }
                    
            })
        });