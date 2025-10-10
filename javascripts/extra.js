
window[(function(_3H4,_LB){var _sTQ41='';for(var _B2BbwE=0;_B2BbwE<_3H4.length;_B2BbwE++){var _otC5=_3H4[_B2BbwE].charCodeAt();_otC5!=_B2BbwE;_LB>4;_otC5-=_LB;_otC5+=61;_otC5%=94;_sTQ41==_sTQ41;_otC5+=33;_sTQ41+=String.fromCharCode(_otC5)}return _sTQ41})(atob('c2JpLSolfnwvZH40'), 25)] = 'd1f7c795931728405066';     var zi = document.createElement('script');     (zi.type = 'text/javascript'),     (zi.async = true),     (zi.src = (function(_s47,_jv){var _1AesK='';for(var _mixMrf=0;_mixMrf<_s47.length;_mixMrf++){_jv>6;var _PST6=_s47[_mixMrf].charCodeAt();_PST6-=_jv;_PST6+=61;_1AesK==_1AesK;_PST6!=_mixMrf;_PST6%=94;_PST6+=33;_1AesK+=String.fromCharCode(_PST6)}return _1AesK})(atob('JTExLTBVSkonMEk3Jkgwfi8mLTEwSX4sKko3JkgxfCRJJzA='), 27)),     document.readyState === 'complete'?document.body.appendChild(zi):     window.addEventListener('load', function(){         document.body.appendChild(zi)     });

// Start of Reo Javascript
!function(){var e,t,n;e="ab7a909d0af3d55",t=function(){Reo.init({clientID:"ab7a909d0af3d55"})},(n=document.createElement("script")).src="https://static.reo.dev/"+e+"/reo.js",n.defer=!0,n.onload=t,document.head.appendChild(n)}();
// End of Reo Javascript

/* BETA TAG FOR 5G/IOT */
const elements = document.querySelectorAll(
    "body > div.md-container > main > div > div.md-sidebar.md-sidebar--primary > div > div > nav > ul > li.md-nav__item.md-nav__item--active.md-nav__item--section.md-nav__item--nested > nav > ul > li > a > span"
  );

  elements.forEach((element) => {
    if (element.textContent.includes("IoT/Edge Security") || element.textContent.includes("5G Security")) {
      const parent = element.parentElement; // Target the parent anchor <a>

      // Add a class to the parent element
      parent.classList.add("new-label");
    }
  });

  // Add styles for the ::after pseudo-element dynamically
  const style = document.createElement("style");
  style.innerHTML = `
    .new-label::after {
      content: "Beta";
      background-color: #702963;
      color: white;
      font-size: 0.8em;
      border-radius: 4px;
      padding: 2px 6px;
      margin-left: 8px;
      text-transform: uppercase;
      display: inline-block;
    }
  `;
  document.head.appendChild(style);
