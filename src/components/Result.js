import React from "react";
import Progress from "../progress";

export default function Result({ percentage, executeScroll }) {
  return (
    <>
      <div className="result">
        <div className="text-center">
          <div className="progress_bar">
            <Progress
              progress={percentage}
              strokeWidth={10}
              reduction={0}
              subtitle="Similarity"
              gradient={[
                { stop: 0.0, color: "#f26965" },
                { stop: 1, color: "#f26965" },
              ]}
            />
          </div>
          <div className="text">
            We found {percentage}% plagiarism in your text
          </div>
        </div>
        <div className="view-result text-right" onClick={executeScroll}>
          View complete result
        </div>
      </div>
    </>
  );
}
