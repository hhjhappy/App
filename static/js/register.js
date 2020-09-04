/*
 * @Description: 
 * @Author: limaochao
 * @Date: 2020-08-23 15:36:32
 * @LastEditTime: 2020-08-24 00:11:19
 */

$(document).ready(function(){
    var canCommit = 0;
    $("#id_Source_ip,#id_Destination_IP").on('keyup', function(){
        console.log('aa');
        var source_ip = $(this).val();
        if(!isValidIP(source_ip)){
            if(!document.getElementById("source_ip_error")){
                $(this).parent("div.form-style-agile").before('<div id="source_ip_error" class="alert alert-danger">ip地址格式错误!</div>');
            } 
        } else {
            $("#source_ip_error").remove();
            canCommit += 1;
        }
    });
    
    $("form#my-form").on('click', "input[type=submit]", function(){
        if(canCommit != 2){
            alert('表单填写不正确！');
        }
    });
    
    $("a#logout").on('click', function(){
        if(!confirm('是否确定退出登录？')){
            return false;
        };
    })
})

function isValidIP(ip) {
    var reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/
    return reg.test(ip);
} 