


$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({

        type:'POST',
        url:'http://127.0.0.1:8000/api/',
        data :{       
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            $('#err-msg').addClass('').text('');
            
            console.log("success");
            if (data.length>1){
                renderHtml(data[0])
                console.log(data);  
                $('#tester-2').html('<h3>'+data[1].name+'</h3>')
            }   
            else{
                renderHtml(data)
                $('#tester-2').html('')
                console.log(data);
            }
        },

        error:function(err){
            console.log(err)
            $('#err-msg').addClass( "alert alert-danger" ).text('There is  nobody in the queue');
            $('#tester-1').text('')
            $('#tester-2').text('')
        }

    })

})



function renderHtml(data){
    $('#tester-1').html('<h3>'+data.name+'</h3>')
}


$( document ).ready(function() {
    console.log('ready')
    $.ajax({


        type:'GET',
        url:'http://127.0.0.1:8000/api/',
        success:function(data){
            
            console.log("ready");
            if (data.length>1){
                
                console.log(data);  
                $('#tester-2').html('<h3>'+data[0].name+'</h3>')
            }
           
            else{
                $('#tester-2').html('<h3>'+data.name+'</h3>')
                console.log(data);
            }
        },
        error:function(err){
            console.log(err)
        }
    
}); 

    });