# comp_announcement_crawling






경북대학교 IT대학 컴퓨터학부
































// Common Javascript
var \_CACHE\_URL = 'http://computer.knu.ac.kr';
var \_PACK\_URL = 'http://computer.knu.ac.kr/pack';
var \_CURRENT\_PAGE = '/06\_sub/02\_sub.html';











 $(window).load(function () {
 $(".main-visual-txt-con").addClass("active-item");
 });
 $(function () {
 dep1 = 0,
 dep2 = 0;

 // window 가로 값따라 메인 비주얼 이미지 변경
 var w\_width = window.innerWidth;

 $("#mainBanner").each(function () {
 if ( w\_width <= 800) {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_pc.jpg","\_m.jpg"));
 }else {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_m.jpg","\_pc.jpg"));
 }
 });

 $(window).resize(function () {
 var w\_width = $(window).width();

 $("#mainBanner").each(function () {
 if ( w\_width <= 800) {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_pc.jpg","\_m.jpg"));
 }else {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_m.jpg","\_pc.jpg"));
 }
 });
 });

 })






$(document).ready(function(){
 $.datepicker.regional['ko'] = {
 closeText: '닫기',
 prevText: '이전달',
 nextText: '다음달',
 currentText: '오늘',
 monthNames: ['1월(JAN)','2월(FEB)','3월(MAR)','4월(APR)','5월(MAY)','6월(JUN)',
 '7월(JUL)','8월(AUG)','9월(SEP)','10월(OCT)','11월(NOV)','12월(DEC)'],
 monthNamesShort: ['1월','2월','3월','4월','5월','6월',
 '7월','8월','9월','10월','11월','12월'],
 dayNames: ['일','월','화','수','목','금','토'],
 dayNamesShort: ['일','월','화','수','목','금','토'],
 dayNamesMin: ['일','월','화','수','목','금','토'],
 weekHeader: 'Wk',
 dateFormat: 'yymmdd',
 firstDay: 0,
 isRTL: false,
 showMonthAfterYear: true,
 yearSuffix: ''};
 $.datepicker.setDefaults($.datepicker.regional['ko']);


 $('.datepicker').datepicker({
 monthNamesShort: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
 dayNamesMin: ['일','월','화','수','목','금','토'],
 weekHeader: 'Wk',
 dateFormat: 'yy-mm-dd',
 autoSize: false,
 changeYear: true,
 changeMonth: true,
 showButtonPanel: true,
 currentText: '오늘 2022-01-17',
 closeText: '닫기'
 });

});



 function execPostcode() {
 new daum.Postcode({
 oncomplete: function(data) {
 // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

 // 각 주소의 노출 규칙에 따라 주소를 조합한다.
 // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
 var fullAddr = ''; // 최종 주소 변수
 var extraAddr = ''; // 조합형 주소 변수

 // 사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
 if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
 fullAddr = data.roadAddress;

 } else { // 사용자가 지번 주소를 선택했을 경우(J)
 fullAddr = data.jibunAddress;
 }

 // 사용자가 선택한 주소가 도로명 타입일때 조합한다.
 if(data.userSelectedType === 'R'){
 //법정동명이 있을 경우 추가한다.
 if(data.bname !== ''){
 extraAddr += data.bname;
 }
 // 건물명이 있을 경우 추가한다.
 if(data.buildingName !== ''){
 extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
 }
 // 조합형주소의 유무에 따라 양쪽에 괄호를 추가하여 최종 주소를 만든다.
 fullAddr += (extraAddr !== '' ? ' ('+ extraAddr +')' : '');
 }

 // 우편번호와 주소 정보를 해당 필드에 넣는다.
 document.getElementById('h\_zip').value = data.zonecode; //5자리 새우편번호 사용
 document.getElementById('h\_addr1').value = fullAddr;

 // 커서를 상세주소 필드로 이동한다.
 document.getElementById('h\_addr2').focus();
 }
 }).open();
 }
 function execPostcode2() {
 new daum.Postcode({
 oncomplete: function(data) {
 // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

 // 각 주소의 노출 규칙에 따라 주소를 조합한다.
 // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
 var fullAddr = ''; // 최종 주소 변수
 var extraAddr = ''; // 조합형 주소 변수

 // 사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
 if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
 fullAddr = data.roadAddress;

 } else { // 사용자가 지번 주소를 선택했을 경우(J)
 fullAddr = data.jibunAddress;
 }

 // 사용자가 선택한 주소가 도로명 타입일때 조합한다.
 if(data.userSelectedType === 'R'){
 //법정동명이 있을 경우 추가한다.
 if(data.bname !== ''){
 extraAddr += data.bname;
 }
 // 건물명이 있을 경우 추가한다.
 if(data.buildingName !== ''){
 extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
 }
 // 조합형주소의 유무에 따라 양쪽에 괄호를 추가하여 최종 주소를 만든다.
 fullAddr += (extraAddr !== '' ? ' ('+ extraAddr +')' : '');
 }

 // 우편번호와 주소 정보를 해당 필드에 넣는다.
 document.getElementById('c\_zip').value = data.zonecode; //5자리 새우편번호 사용
 document.getElementById('c\_addr1').value = fullAddr;

 // 커서를 상세주소 필드로 이동한다.
 document.getElementById('c\_addr2').focus();
 }
 }).open();
 }

 $(function () {
 dep1 = 06,
 dep2 = 01;

 // sub2\_num 변수가 있을때 ( 3차메뉴 )
 dep3 = 06;
 /* cool 추가 */
 if ( dep1 > 0 && dep2 > 0 ) { 
 $("#gnb > ul").children("li.gnb-1dep").eq(dep1-1).addClass("active");
 }
 if(dep1 !=0 && dep2 !=0){
 $(".visual-txt-inner").removeClass("open");
 $(".visual-txt-inner-"+dep1).addClass("open");
 $(".main-header-shadow").css("display", "none");
 } 

 if (dep1 == 10 || dep1 == 11) {
 $("#visual").css("display", "none");
 $("#container").addClass("member");
 }

 if(dep1 != 10) {
 var tab\_length = $(".snb li").length;
 $(".snb li").css("width",(100/tab\_length)+"%");
 }

 if(dep1 == 0) {
 $(".snb").addClass("lot");
 }

 if(dep1 == 0 || dep1 == 8 || dep1 == 12 ) {
 $("#subMenu").css("display", "none");
 }

 if(!(dep1==0 && dep2 == 0)){
 $("#rightBar").addClass("sub");
 }

 });


 $(window).load(function () {
 $("#visual").addClass("active");
 });




 [본문바로가기](#mainContainer) 








## 주메뉴



  * [![](../img/include/logo-off.png)](../main/)
* [*학부소개 학부소개*](../01_sub/01_sub.html)


	+ [인사말](../01_sub/01_sub.html)
	+ [교육목표](../01_sub/02_sub.html)
	+ [연혁](../01_sub/03_sub.html)
	+ [현황](../01_sub/04_sub.html)
	+ [위치 및 연락처](../01_sub/05_sub.html)
	+ [학부관련연구소](../01_sub/06_sub.html)
* [*구성원 구성원*](../02_sub/01_sub.html)


	+ [교수진](../02_sub/01_sub.html)
	+ [초빙교수](../02_sub/02_sub.html)
	+ [명예교수](../02_sub/03_sub.html)
	+ [직원](../02_sub/04_sub.html)
* [*학부 학부*](../03_sub/07_sub.html)


	+ [입학정보](../03_sub/07_sub.html)
	+ [학부과정 소개](../03_sub/01_sub.html)
	+ [심화컴퓨터공학](../03_sub/02_sub.html)
	+ [글로벌SW융합](../03_sub/03_sub.html)
	+ [SW연계/융합](../03_sub/04_sub.html)
	+ [입시 FAQ](../03_sub/05_sub.html)
* [*대학원 대학원*](../04_sub/01_sub.html)


	+ [입학정보](../04_sub/02_sub.html)
	+ [연구](../04_sub/01_sub.html)
	+ [일반대학원 (BK21)](../04_sub/03_sub.html)
	+ [산업대학원](../04_sub/04_sub.html)
	+ [정보보호학과](../04_sub/05_sub.html)
	+ [데이터융합컴퓨팅학과](../04_sub/07_sub.html)
	+ [계약학과](../04_sub/06_sub.html)
* [*국제교류 국제교류*](../05_sub/01_sub.html)


	+ [해외복수학위](../05_sub/01_sub.html#a)
	+ [교환학생프로그렘](../05_sub/01_sub.html#b)
	+ [국제화프로그램](../05_sub/01_sub.html#c)
	+ [해외학술교류현황](../05_sub/01_sub.html#d)
* [*커뮤니티 커뮤니티*](../06_sub/01_sub.html)


	+ [뉴스](../06_sub/01_sub.html)
	+ [공지사항](../06_sub/02_sub.html)
	+ [취업정보](../06_sub/03_sub.html)
	+ [학부인재모집](../06_sub/04_sub.html)
	+ [세미나](../06_sub/05_sub.html)
	+ [학생회](../06_sub/06_sub.html)
	+ [동아리](../06_sub/07_sub.html)




 [![](../img/include/m-logo.png)](../main/) 





[ENG](http://computer.knu.ac.kr/eng/main/index.html)



[![](../img/include/icon-logout.png)](../07_sub/01_sub.html)





[ENG](http://computer.knu.ac.kr/eng/main/index.html)

[![](../img/include/icon-logout.png)](../07_sub/01_sub.html)

 

## 주메뉴


* [학부소개](javascript:;)
	+ [인사말](../01_sub/01_sub.html)
	+ [교육목표](../01_sub/02_sub.html)
	+ [연혁](../01_sub/03_sub.html)
	+ [현황](../01_sub/04_sub.html)
	+ [위치 및 연락처](../01_sub/05_sub.html)
	+ [학부관련연구소](../01_sub/06_sub.html)
* [구성원](javascript:;)
	+ [교수진](../02_sub/01_sub.html)
	+ [초빙교수](../02_sub/02_sub.html)
	+ [명예교수](../02_sub/03_sub.html)
	+ [직원](../02_sub/04_sub.html)
* [학부](javascript:;)
	+ [입학정보](../03_sub/07_sub.html)
	+ [학부과정 소개](../03_sub/01_sub.html)
	+ [심화컴퓨터공학](../03_sub/02_sub.html)
	+ [글로벌SW융합](../03_sub/03_sub.html)
	+ [SW연계/융합](../03_sub/04_sub.html)
	+ [입시 FAQ](../03_sub/05_sub.html)
* [대학원](javascript:;)
	+ [입학정보](../04_sub/02_sub.html)
	+ [연구](../04_sub/01_sub.html)
	+ [일반대학원 (BK21)](../04_sub/03_sub.html)
	+ [산업대학원](../04_sub/04_sub.html)
	+ [정보보호학과](../04_sub/05_sub.html)
	+ [데이터융합컴퓨팅학과](../04_sub/07_sub.html)
	+ [계약학과](../04_sub/06_sub.html)
* [국제교류](javascript:;)
	+ [해외복수학위](../05_sub/01_sub.html#a)
	+ [교환학생프로그렘](../05_sub/01_sub.html#b)
	+ [국제화프로그램](../05_sub/01_sub.html#c)
	+ [해외학술교류현황](../05_sub/01_sub.html#d)
* [커뮤니티](javascript:;)
	+ [뉴스](../06_sub/01_sub.html)
	+ [공지사항](../06_sub/02_sub.html)
	+ [취업정보](../06_sub/03_sub.html)
	+ [학부인재모집](../06_sub/04_sub.html)
	+ [세미나](../06_sub/05_sub.html)
	+ [학생회](../06_sub/06_sub.html)
	+ [동아리](../06_sub/07_sub.html)




 









##  커뮤니티



더 높고 더 넓게 날며 더 넓은 열린 세상을 보는


경북대학교 IT대학 컴퓨터학부











### 공지사항


**

* [뉴스](01_sub.html)
* [공지사항](02_sub.html)
* [취업정보](03_sub.html)
* [학부인재모집](04_sub.html)
* [세미나](05_sub.html)
* [학생회](06_sub.html)
* [동아리](07_sub.html)




[**](01_sub.html)
[**](03_sub.html)













* [뉴스](01_sub.html)
* [공지사항](02_sub.html)
* [취업정보](03_sub.html)
* [학부인재모집](04_sub.html)
* [세미나](05_sub.html)
* [학생회](06_sub.html)
* [동아리](07_sub.html)
  



 **공지사항**
경북대학교 IT대학 컴퓨터학부에 오신것을 환영합니다.






* [전체 공지](02_sub.html)
* [학사](02_sub_2.html)
* [심컴](02_sub_3.html)
* [글솝](02_sub_4.html)
* [대학원](02_sub_6.html)
* [대학원 계약학과](02_sub_7.html)









function bbs\_category(value){
 location.href='?category='+value+'&bbs\_code=Site\_BBS\_25';
}
function step\_move(no,mode){
 location.href="?bbs\_cmd=step\_exe&mode="+mode+"&no="+no+"&key=&keyfield=&category=&bbs\_code=Site\_BBS\_25";
}
function preview\_window(image,tbl){
 window.open('/pack/bbs/image\_preview.php?tbl='+tbl+'&image='+image,"previewWin",'width='+300+',height='+200+',top='+(screen.height-200)/2+',left='+(screen.width-300)/2+',toolbar=no,resizable=no,status=no,scrollbars=yes');
}
function preview\_window2(image,tbl){
 window.open('/pack/bbs/image\_preview2.php?tbl='+tbl+'&image='+image,"previewWin",'width='+300+',height='+200+',top='+(screen.height-200)/2+',left='+(screen.width-300)/2+',toolbar=no,resizable=no,status=no');
}
function img\_step\_move(file\_no,mode){
 location.href="?no=3665&fpage=&page=1&bbs\_cmd=img\_step\_exe&mode="+mode+"&file\_no="+file\_no+"&key=&keyfield=&category=&bbs\_code=Site\_BBS\_25";
}












[모집] 대경권 SW산학프로젝트 경진대회 개최 안내





작성자
방원길


작성일
2021-12-30 16:55


조회수
1,180


첨부파일 : [대경권SW산학프로젝트경진대회참가신청서양식.hwp](/pack/bbs/down.php?f_name=Q0dUVlpFWVVaVXZLcxUVbktTVQ==&o_name=대경권SW산학프로젝트경진대회참가신청서양식.hwp&tbl=Site_BBS_25) [15 KB]첨부파일 : [웹포스터.JPG](/pack/bbs/down.php?f_name=QkdUVlpFWVVbVXdOchURbklUQg==&o_name=웹포스터.JPG&tbl=Site_BBS_25) [1,034 KB]


﻿﻿지역선도대학육성사업에서는 지역SW산업체와의 산학프로젝트 수행성과 공유 및 실무역량 강화를 위해

대경권 SW산학프로젝트 경진대회를 개최합니다.

  


﻿  


![](http://cse.knu.ac.kr/_files/userfile/image/20211230165709200195.jpg)

  








[목록](?key=&keyfield=&category=&page=1&bbs_code=Site_BBS_25)
[이전글](?bbs_cmd=view&page=1&key=&keyfield=&category=&no=3664&bbs_code=Site_BBS_25)
[다음글](?bbs_cmd=view&page=1&key=&keyfield=&category=&no=3666&bbs_code=Site_BBS_25)

















 $(document).on('ready',function () {
 $('.slider-for').slick({
 slidesToShow: 1,
 slidesToScroll: 1,
 arrows: false,
 fade: true,
 asNavFor: '.slider-nav'
 });
 $('.slider-nav').slick({
 slidesToShow: 1,
 slidesToScroll: 1,
 asNavFor: '.slider-for',
 dots: true,
 //centerMode: true,
 focusOnSelect: true,
 autoplay: true,
 fade: true,
 autoplaySpeed : 4500,
 easing : 'easeOutCubic',
 });

 var w\_width = window.innerWidth;
 
 $(".slick-track .visual-list-img").each(function () {
 if ( w\_width <= 749) {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_pc.jpg","\_m.jpg"));
 }else {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_m.jpg","\_pc.jpg"));
 }
 });
 
 $(window).resize(function () {
 var w\_width = $(window).width();
 
 $(".slick-track .visual-list-img").each(function () {
 if ( w\_width <= 749) {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_pc.jpg","\_m.jpg"));
 }else {
 $(this).children("img").attr("src",$(this).children("img").attr("src").replace("\_m.jpg","\_pc.jpg"));
 }
 });
 });
 })


$(document).ready(function(){
 /* *********************** 탭 공통 ************************ */
 $(".cm-tab-container").each(function () {
 var $cmTabList = $(this).children(".cm-tab-list");
 var $cmTabListli = $cmTabList.find("li");
 var $cmConWrapper = $(this).children(".cm-tab-content-wrapper");
 var $cmContent = $cmConWrapper.children(".cm-tab-con");
 
 
 // 탭 영역 숨기고 selected 클래스가 있는 영역만 보이게
 var $selectCon = $cmTabList.find("li.selected").find("a").attr("href");
 $cmContent.hide();
 $($selectCon).show();
 
 $cmTabListli.children("a").click(function () {
 if ( !$(this).parent().hasClass("selected")) {
 var visibleCon = $(this).attr("href");
 $cmTabListli.removeClass("selected");
 $(this).parent("li").addClass("selected");
 $cmContent.hide();
 $(visibleCon).fadeIn();
 }
 return false;
 });
 });
})


 $(function () {
 dep1 = 0,
 dep2 = 0;

 // 탑배너 롤링
 $(".top-banner-list-con").slick({
 dots: true,
 infinite: true,
 arrows:false,
 pauseOnHover:false,
 autoplay:true,
 autoplaySpeed: 5000,
 slidesToShow: 1,
 slidesToScroll: 1,
 fade:true
 });
 // 탑배너 닫기
 $(".banner-close-btn .close-btn").click(function () {
 $("#topBanner").slideUp();
 });
 });

function setCookie( name, value, expiredays )
{
 var todayDate = new Date();
 todayDate.setDate( todayDate.getDate() + expiredays );
 document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

function closeWin(){
 if ( document.popuptop\_form.popup\_end.checked ) {
 setCookie( 'POPUPTOP\_COOKIE', 'NO', 1 );//쿠기 저장 기간은 1일로 한다.
 }
} 



 /* Footer
------------------------------------------------------ */
.section{position:relative}
#footer{clear:both;width:100%;padding:0;}
#footer:after {display:block;visibility:hidden;clear:both;content:""}
#footer .section01 {background:#fff;position:relative;height:68px;}
#footer .section01 h1 {position:absolute;top:15px;left:0;}
#footer .section01 .sns {position:absolute;top:20px;right:0;}
#footer .section02 {background:#313437;position:relative;height:52px;border-bottom:1px solid #252526;}
#footer .section02 .link {position:absolute;top:15px;left:0;}
#footer .section02 .link a {color:#aaa; padding:0 15px;border-right:1px solid #6d6d6e; font-size:12px}
#footer .section02 .link a:last-child {border-right:none;}

#footer .section02 .icon {position:absolute; right:0; text-align:right}
#footer .section02 .icon a {float: right;}
#footer .section02 .icon a:last-child {right:0;}


#footer .section03 {background:#3d4044;position:relative;padding:30px 0 50px 0;}
#footer .section03 .select {position:absolute;top:0px;right:0;}
#footer .section03 .select select {background:#3d4044;color:#fff; padding:10px 10px;border:1px solid #6d6d6e;width:180px; }
#footer .address{display:inline-block; margin:0 0 0 18px; line-height:22px; color:#e1e1e1; font-weight:300; letter-spacing:0px; font-size:14px}


/* 푸터 */
#m-footerInner{width:100%; display:none;}
#m-footerInner .footer-top{padding:3% 5%; background-color:#2b2b2c;}
.footer-top ul.footer-list{width:100%; margin:0 auto;}
.footer-top ul.footer-list li{display:inline-block; vertical-align:top; width:24%; text-align:center;}
.footer-top ul.footer-list li a{font-size:16px; color:#aaa;}
.footer-top ul.footer-list li:first-child a{color:#aaa;}
#m-footerInner .footer-bottom{width:100%; padding:5% 0 10% 0; background-color:#353536; text-align:center;}
.footer-bottom > p, .footer-bottom > span{display:inline-block; width:96%; margin:0 auto; text-align:center; color:#fff;}
.footer-bottom > p{margin-bottom:3%; line-height:22px;}
.footer-bottom > span > strong{font-weight:normal; color:#c3c3c3;}
#m-footerInner .footer-sns{width:94%; padding:3%; background:url(/images/layout/footer\_logo.png) no-repeat 3% center; text-align:right;}
.footer-sns .sns-list{display:inline-block; width:49%; text-align:right;}
.footer-sns .sns-list li{display:inline-block; vertical-align:top; padding:0 2%;}
.footer-sns .sns-list li .fa{font-size:30px; color:#000;}

/* footer :: familybox */
.familysite-box{position:relative; width:240px; float:right; /*margin-top:25px;*/}
.familysite-box > a{display:block; height:40px; line-height:40px; text-indent:20px; border:1px solid #b0b0b0; background-color:#3d4044; color:#fff; font-size:14px;}
.familysite-box > a i{position:absolute; right:15px; top:7px;}
.family-list{position:absolute; bottom:30px; left:0px; width:238px; padding:10px 0; background-color:#3d4044; border:1px solid #b0b0b0; border-bottom:0; z-index:11; display:none; }
.family-list a{display:block; padding:10px 15px; color:#fff; letter-spacing:-0.5px; font-size:14px;}
.family-list a:hover{color:#c48b3a}

@media all and (max-width:768px){
 /* FOOTER */
 .footer-bottom > p{font-size:12px; line-height:20px;}
 .footer-bottom > span{font-size:10px;}
}
@media all and (max-width:1220px){
 #m-gnb{display:block; width:100%; height:100%; position:fixed; top:0px; right:-100%; z-index:9999; overflow-y:auto; overflow-x:hidden; background:url(/images/layout/m\_gnb\_bg.jpg) repeat-y right top; background-size:70% auto; max-width:400px;}
 /* Footer
 ------------------------------------------------------ */
 #footerInner{display:none;}
 #m-footerInner{display:block;}
 }
 
 @media all and (max-width:479px){
 
 /* footer
 ------------------------------------------------------ */
 #m-footerInner .footer-top{padding:4% 0;}
 .footer-top ul.footer-list li{width:49%; margin-bottom:2%;}
 .footer-top ul.footer-list li.marn{margin-bottom:0;}
 .footer-top ul.footer-list li a{font-size:12px;}
 #m-footerInner .footer-sns{background-size:150px auto;}
 .footer-sns .sns-list li .fa{font-size:20px; color:#000;}
 .footer-sns .sns-list li img{width:13px;}
 }
 
 
 
  






[개인정보처리방침](../07_sub/04_sub.html) 
[이메일무단수집거부](../07_sub/05_sub.html) 
[오시는 길](../01_sub/05_sub.html)


[![](../img/include/instagram.png)](https://www.instagram.com/knu_cse_pr/)
[![](../img/include/facebook.png)](https://www.facebook.com/CSEatKNU/)





경북대학교 IT대학 컴퓨터학부  





학부관련연구소**
* [공학설계연구소](http://www.knuiedt.re.kr "새창으로열기")
* [뇌과학연구소](http://brain.knu.ac.kr "새창으로열기")
* [디지털아트컨텐츠연구소](http://daci.knu.ac.kr "새창으로열기")
* [로봇산업진흥센터](http://robic.knu.ac.kr/ "새창으로열기")
* [모바일디스플레이산학연센터](http://www.necst.or.kr/ "새창으로열기")
* [산업기술연구소](http://www.escrc.re.kr/ "새창으로열기")
* [소프트웨어기술연구소](http://selab.knu.ac.kr/soft/?mid=welcome "새창으로열기")
* [의료정보원천기술연구소](#)
* [임베디드소프트웨어연구센터](http://www.escrc.re.kr/ "새창으로열기")
* [전자기술연구소](http://iet.knu.ac.kr/ "새창으로열기")
* [자율군집소프트웨어 플랫폼 연구센터](http://csos.knu.ac.kr/ "새창으로열기")
* [초연결융합기술연구소](http://connected.knu.ac.kr/ "새창으로열기")




바로가기**
* [SW중심대학사업단](http://swedu.knu.ac.kr/ "새창으로열기")
* [프라임사업단](http://prime.knu.ac.kr/ "새창으로열기")
* [BK21플러스사업단](http://bk21plus.knu.ac.kr/index.php "새창으로열기")
* [LINC사업단](http://linc.knu.ac.kr/ "새창으로열기")
* [KNU ABEEK](http://abeek.knu.ac.kr/ "새창으로열기")
* [소프트웨어교육센터](http://swedu.knu.ac.kr "새창으로열기")
* [외국학술지지원센터](http://fric.knu.ac.kr/new/ "새창으로열기")
* [HuStar ICT 혁신대학사업단](http://hustar-ict.knu.ac.kr "새창으로열기")












* 
* 
* 
* ![](https://kast.or.kr/images/layout/icon_blog.png)
* 




* [개인정보처리방침](../07_sub/04_sub.html)
* [이메일무단수집거부](../07_sub/05_sub.html)





[![](../img/include/instagram.png)](https://www.instagram.com/knu_cse_pr/)
[![](../img/include/facebook.png)](https://www.facebook.com/CSEatKNU/)



대구광역시 북구 대학로 80 / IT대학 융복합관 317호(건물번호 : 415)  

Tel : 053-950-5550. 6370 / Fax : 053-957-4846  

 E-mail : scse@knu.ac.kr


 **Copyright 2019**  KNU CSE  **All rights reserved**







