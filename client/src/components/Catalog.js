import React, { Component } from "react";
import "../styles/catalog.css";
import * as constants from "../constants/consts.js";
import Item from "./Item";
import SearchBar from "./SearchBar";

class Catalog extends Component {
    constructor() {
        super();
        this.state = {
            searchText: "",
            shouldRentedContainer: false,
        };
    }
    toggleRentStatus = (movieId) => this.props.toggleRentStatus(movieId);
    shouldRentedContainer = () => {
        const movie = this.props.movies.find(
            (movie) => movie.isRented === true
        );
        this.setState({
            shouldRentedContainer: movie === undefined ? false : true,
        });
    };

    filterSearchBar = (text) =>
        this.setState({ searchText: text.toUpperCase() });

    displayMovies = (rentMovies) => {
        let movies = this.props.movies;
        if (rentMovies) {
            movies = movies.filter((movie) => movie.isRented === true);
        }
        return movies
            .filter((movie) =>
                movie.title.toUpperCase().includes(this.state.searchText)
            )
            .map((movie) => (
                <Item
                    key={movie.id}
                    movie={movie}
                    toggleRentStatus={this.toggleRentStatus}
                    checkRentContainer={this.shouldRentedContainer}
                    rentItems={rentMovies}
                />
            ));
    };

    render() {
        const state = this.state;
        const moviesComponants = this.displayMovies(false);
        const moviesRentalComponants =
            state.shouldRentedContainer === true
                ? this.displayMovies(true)
                : null;

        const searchComponant = (
            <SearchBar text={state.searchText} setText={this.filterSearchBar} />
        );
        console.log("budget", this.props.budget);
        return (
            <div className="catalog-container">
                <h1>{this.props.budget}</h1>
                {searchComponant}

                {state.shouldRentedContainer === true ? (
                    <div className="catalog-body">
                        <h1>{constants.RENTAL_MOVIES}</h1>
                        {moviesRentalComponants}
                    </div>
                ) : null}

                <div className="catalog-body">
                    <h1>{constants.CATALOG_MOVIES}</h1>
                    {moviesComponants}
                </div>
            </div>
        );
    }
}

export default Catalog;
