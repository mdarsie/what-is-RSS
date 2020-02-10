import React from 'react'
import './index.css'

export default function Article(props) {
    return (
        <div className="article-container">
            <div className="content-container">
                <div className="feed">
                    {props.feed} 
                    </div>
                <div className="articleTitle">{props.article_title}</div>
                
    
            </div>
       
    )
}