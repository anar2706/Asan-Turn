
     setInterval(my_func,500); 

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
    
}); 
    }
