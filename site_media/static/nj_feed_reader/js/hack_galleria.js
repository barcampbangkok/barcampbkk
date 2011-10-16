/**
 * Created by PyCharm.
 * User: natty
 * Date: 12/10/2011
 * Time: 20:17
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){
    Galleria().ready(function (options){
        $('div.galleria-info').click(function () {
            $(this).css("display","block");$('div.galleria-info-text').css("display","block");
            $('div.galleria-info-link').css("display","none");
            $('div.galleria-info-close').css("display","none");
          });
    });
});
