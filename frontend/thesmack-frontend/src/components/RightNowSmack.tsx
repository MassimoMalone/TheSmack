// src/components/RightNowSmack.tsx

import React from "react";
import "./RightNowSmack.css";

const RightNowSmack: React.FC = () => {
  const featuredSmack = {
    date: "02-Oct-25",
    time: "12:30PM",
    author: "Lane's",
    update:
      "Okay, watching daytime TV makes me never want to be sick enough to miss work ever again.",
    mood: "Sick",
    moodIcon: "🤒",
  };

  return (
    <div className="right-now-container">
      {/* The blue header text, styled to look retro */}
      <div className="right-now-header">THE RIGHT NOW</div>

      <div className="right-now-content">
        <div className="date-time">
          {featuredSmack.date} {featuredSmack.time}
        </div>

        <div className="profile-info">
          <div className="avatar-placeholder"></div>
          <div className="author-update">
            <span className="author-name">{featuredSmack.author}</span>
            <span className="latest-update">Newest Update:</span>
          </div>
        </div>

        <p className="smack-blurb">{featuredSmack.update}</p>

        <div className="smack-mood">
          <span className="mood-label">Mood:</span>
          <span className="mood-icon">{featuredSmack.moodIcon}</span>
          <span className="mood-text">{featuredSmack.mood}</span>
        </div>
      </div>
    </div>
  );
};

export default RightNowSmack;
