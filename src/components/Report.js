import React from "react";
import { useEffect } from "react";

export default function Report({ reportRef, resultText }) {
  //   window.onload = function () {
  //     document.getElementById("resulttext").innerHTML = resultText;
  //   };

  useEffect(() => {
    document.getElementById("resulttext").innerHTML = resultText;
  }, [resultText]);

  return (
    <div className="report my-3" ref={reportRef}>
      <div className="scan-report pr-3 py-4">
        <h4>Plagiarism Scan Report</h4>
      </div>
      <div className="sources mb-4">View Plagiarised Sources</div>
      <div class="col-md-4 col-sm-6 float-left p-0">
        <span id="chars">
          {" "}
          <strong> Characters: </strong> <span>867</span>{" "}
        </span>
      </div>
      <div class="col-md-4 col-sm-6 float-left p-0">
        <span id="words" class="pl-md-3 pl-0">
          {" "}
          <strong> Words: </strong> <span>137</span>{" "}
        </span>
      </div>
      <div class="col-md-4 col-sm-6 float-left p-0">
        <span id="sentencesris">
          {" "}
          <strong> Sentences: </strong> <span> 20 </span>{" "}
        </span>
      </div>
      <div class="clearfix"></div>
      <hr />
      <div className="result-text text-justify" id="resulttext">
        {resultText}
        <mark>
          The SPIDER_MIDDLEWARES setting is merged with the
          SPIDER_MIDDLEWARES_BASE setting defined in Scrapy (and not meant to be
          overridden) and then sorted by order to get the final sorted list of
          enabled middleware.
        </mark>{" "}
        So for example, if at mid-semester or much later on you find out that
        your proposed scope can’t be achieved by the end of the semester.
      </div>
    </div>
  );
}
