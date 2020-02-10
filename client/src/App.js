import React from "react";
import axios from "axios";
import "./App.css";
import Article from "./components/Feed";
import Feed from "./components/AllFeeds"

class App extends React.Component {
  state = {
    articles: [],
    feeds: [],
    newFeed: {
      feed_title: "",
      feed_description: "",
      feed_link: "",
      group: "none"
    }
  };

  componentDidMount() {
    this.loadMegaData();
    this.loadFeedData();
  }

  loadMegaData = async () => {
    try {
      const res = await axios.get("/api/v1/article");
      this.setState({ articles: res.data.reverse() });
    } catch (err) {
      console.log("Failed to retrieve data");
    }
  };

  loadFeedData = async () => {
    try {
      const res = await axios.get("/api/v1/feed");
      this.setState({ feeds: res.data});
    } catch (err) {
      console.log("Failed to retrieve data");
    }
  };

  onNewFeedAdd = event => {
    const value = event.target.value;
    const name = event.target.name;
    const newState = { ...this.state };

    newState.newFeed[name] = value;

    this.setState(newState);
  };

  onNewFeed = () => {
    axios.post("/api/v1/feed/", this.state.newFeed).then(() => {
      this.loadMegaData();
    });
  };

  render() {
    return (
      <div>
        <h1>What is RSS!?</h1>
        {
        this.state.feeds.map(feed => {
          return (
            <Feed
              feed_title={feed.feed_title}
              feed_link={feed.feed_link}
            />
          );
        })}
        
        <div className="new-feed">
          <input
            className="new-feed-link"
            placeholder="Paste the RSS URL here"
            name="feed_link"
            onChange={this.onNewFeedAdd}
            value={this.state.newFeed.feed_link}
          />

          <input
            type="text"
            placeholder="Name of Feed"
            name="feed_title"
            onChange={this.onNewFeedAdd}
            value={this.state.newFeed.feed_title}
          />

          <input
            type="text"
            placeholder="Description"
            name="feed_description"
            onChange={this.onNewFeedAdd}
            value={this.state.newFeed.feed_description}
          />

          <button className="add-feed-button" onClick={this.onNewFeed}>
            Add Feed!
          </button>
        </div>
        {
        this.state.articles.map(article => {
          return (
            <Article
              feed={article.feed.feed_title}
              article_title={article.article_title}
              article_link={article.article_link}
            />
          );
        })}
         

      </div>
      
    );
  }
}

export default App;
