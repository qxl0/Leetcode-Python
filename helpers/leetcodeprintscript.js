var jq = document.createElement("script");
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(jq);

window.setTimeout(function () {
  jQuery.noConflict();
  contentJquery = jQuery(".content__QRGW");
  contentJquery = contentJquery.children(0)[0];
  jQuery("body").empty();
  jQuery("body").html(contentJquery);

  var fontsize = 20;

  window.setTimeout(function () {
    jQuery("body").find("*").css({ "font-size": fontsize });
    iframes = jQuery("iframe");

    for (i = 0; i < iframes.length; i++) {
      iframe = iframes[i];
      iframe = jQuery(iframe);
      iframe
        .contents()
        .find("*")
        .css({ "font-size": fontsize - 5 });
      iframe.height(iframe.contents().outerHeight() + 500);
    }

    buttons = jQuery(".lang-btn-set button");
    for (i = 0; i < buttons.length; i++) {
      button = buttons[i];
      button = jQuery(button);
      if (button.text() == "Java") {
        button.click();
      }
    }

    jQuery("img").width(300);
  }, 1000);
}, 1000);
