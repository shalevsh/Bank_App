import React, { Component } from "react";
import "../styles/searchBar.css";

class SearchBar extends Component {
    inputHadler = (event) => this.props.setText(event.target.value);
    render() {
        return (
            <input
                placeholder="insert a name ..."
                className="text-input"
                onChange={this.inputHadler}
                value={this.props.text}
            ></input>
        );
    }
}

export default SearchBar;
