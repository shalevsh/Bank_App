import React, { Component } from "react";
import "../styles/description.css";

class Description extends Component {
    render() {
        return (
            <div className="item-description-container">
                <h1 className="item-description-title">
                    {this.props.movie.title}
                </h1>
                <img
                    className="item-image"
                    src={this.props.movie.img}
                    alt={this.props.movie.title}
                />
                <div className="item-description-content">
                    {this.props.movie.descrShort}
                </div>
            </div>
        );
    }
}

export default Description;
