import React from 'react'
import './index.css'

export default function Article(props) {
    return (
        <div className="article-container">
            <div className="article-title">
                <a href={props.article_link}>{props.article_title}</a>
            </div>
                <div className="parent-info">
                    <h3>{props.feed_title}</h3><br></br>
                    <h2>{props.collection}</h2>
               </div>
        </div>)       
}
