/**
 * Created by PyCharm.
 * User: jackdreilly
 * Date: 8/23/11
 * Time: 1:27 AM
 * To change this template use File | Settings | File Templates.
 */

$(function() {
    if ($('.modal').length > 0) {
        $('.modal a.close').click(function() {
            var modal = $('.modal')[0];
            modal.parentNode.removeChild(modal);
            $('body').removeClass('modal-backdrop');
        });
        $('body').addClass('modal-backdrop');
    }
    $("table").tablesorter({ sortList: [[1,0]] });
    $('.household-create').mouseenter(function(){
            $('.popover').css('visibility','visible');
        });
    $('.household-create').mouseleave(function(){
            $('.popover').css('visibility','hidden');
        });
    $('.popover').css('visibility','hidden');


});