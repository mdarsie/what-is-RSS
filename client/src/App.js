import React from "react";
import axios from "axios";
import "./App.css";
import reader from "./components/reader";

class App extends React.Component {
  state = {
    groups: [],
    feeds: [],
    article: []
  };

  componentDidMount() {
    this.loadGroupData();
    this.loadFeedData();
    this.loadArticleData();
  }

  loadGroupData = async () => {
    try {
      const res = await axios.get("/api/v1/group");
      this.setState({ group: res.data });
    } catch (err) {
      console.log("Failed to retrieve data");
    }
  };

  loadFeedData = async () => {
    try {
      const res = await axios.get("/api/v1/feed");
      this.setState({ feed: res.data });
    } catch (err) {
      console.log("Failed to retrieve data");
    }
  };

  loadArticleData = async () => {
    try {
      const res = await axios.get("/api/v1/article");
      this.setState({ article: res.data.reverse() });
    } catch (err) {
      console.log("Failed to retrieve data");
    }
  };

  render() {
    return (
      <div>
        <h1>What is RSS!?</h1>
        <div className="navbar-container">
          <div className="group">
            {this.state.groups.map(group => {
              return <group 
              group={group.collection} 
              feed={group.feed.feed_title}
              />;
            })}
          </div>
        </div>
        {this.state.articles.map(article => {
          return (
            <article
              title={article.article_title}
              description={article.article_description}
              link={article.article_link}
            />
          );
        })}
      </div>
    );
  }
}

export default App;

