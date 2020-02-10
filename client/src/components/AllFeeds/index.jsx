import React from "react";
import "./index.css";

export default function Feed(props) {
  return (
    <div className="navbar-container">
      <div className="feed">
        <a href={props.feed_link}>{props.feed_title}</a>
      </div>
    </div>
  );
}