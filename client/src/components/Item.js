import React, { Component } from "react";
import "../styles/item.css";
import { Link } from "react-router-dom";

class Item extends Component {
    constructor() {
        super();
        this.state = {
            btnText: "+",
        };
    }
    toggleRentStatus = () => {
        const movieId = this.props.movie.id;
        const state = this.state;
        this.props.toggleRentStatus(movieId);
        this.props.checkRentContainer();
        state.btnText === "+"
            ? this.setState({ btnText: "-" })
            : this.setState({ btnText: "+" });
    };

    render() {
        const movie = this.props.movie;
        const state = this.state;
        return (
            <div className="item-container">
                <div className="item-header">{movie.title}</div>
                <div className="item-body">
                    <Link to={`/movies/${movie.id}`}>
                        <img
                            className="item-image"
                            src={movie.img}
                            alt={movie.title}
                        />
                    </Link>
                    {this.props.rentItems ? null : (
                        <button
                            className="rent-button"
                            onClick={this.toggleRentStatus}
                        >
                            {state.btnText}
                        </button>
                    )}
                </div>
            </div>
        );
    }
}

export default Item;
