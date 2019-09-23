


$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({

        type:'POST',
        url:'http://127.0.0.1:8000/api/',
        data :{       
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            op_id:$('#datas').data('pk')
        },
        success:function(data){
            $('#err-msg').addClass('').text('');
            
            console.log("success");
            if (data.length>1){
                renderHtml(data[0])
                $('#tester-2').html('<h3>---'+data[1].name+' '+data[1].surname+' Code:'+ data[1].code+'---</h3>')
            }   
            else{
                renderHtml(data)
                $('#tester-2').html('')
            }
        },

        error:function(err){
            console.log(err)
            $('#err-msg').addClass( "alert alert-danger" ).text('There is  nobody in the queue');
            $('#tester-1').text('')
            $('#tester-2').text('')
            $('#np').text('')
            $('#cr').text('')
        }

    })

})



function renderHtml(data){
    $('#tester-1').html('<h3>---'+data.name+' '+data.surname+' Code:'+ data.code+'---</h3>')
}


setInterval(my_func,1000); 

function my_func(){
    $.ajax({


        type:'GET',
        url:'http://127.0.0.1:8000/api/',
        success:function(data){
            
            if (data.length>1){
                
                $('#tester-2').html('<h3>---'+data[0].name+' '+data[0].surname+' Code:'+ data[0].code+'---</h3>')
            }
           
            else{
                $('#tester-2').html('<h3>---'+data.name+' '+data.surname+' Code:'+ data.code+'---</h3>')
            }
        },
        error:function(err){
            console.log(err)
            $('#np').text('')
            $('#cr').text('')
        }
    
}

    )};
    

