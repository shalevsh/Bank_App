import React, { Component } from "react";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Home from "./components/Home.js";
import Catalog from "./components/Catalog.js";
import NavBar from "./components/NavBar.js";
import Description from "./components/Description.js";
import { movies } from "./data/mockData.js";
import { users } from "./data/mockData.js";

class App extends Component {
    constructor() {
        super();
        this.state = {
            movies,
            users,
            user: {},
        };
    }

    changeUser = (currentUser) => {
        this.setState({ user: currentUser });
    };
    updateRentStatus = (movieId) => {
        const movies = [...this.state.movies];
        const movie = movies.find((movie) => movie.id === movieId);
        movie.isRented = !movie.isRented;
        this.setState({ movies });
    };
    updateBudget = (userName, price) => {
        let updatedBudget = false;
        const newUsers = [...this.state.users];
        const currUser = newUsers.find((u) => u.name === userName);
        if (currUser.budget - price >= 0) {
            currUser.budget = currUser.budget - price;
            this.setState({ users: newUsers });
            updatedBudget = true;
        }
        return updatedBudget;
    };
    render() {
        const state = this.state;
        return (
            <Router>
                <div className="app-container">
                    <NavBar user={state.user} />
                    <Route
                        path="/"
                        exact
                        render={() => (
                            <Home
                                users={state.users}
                                changeUser={this.changeUser}
                            />
                        )}
                    />
                    <Route
                        path="/catalog"
                        exact
                        render={() => (
                            <Catalog
                                movies={state.movies}
                                toggleRentStatus={this.updateRentStatus}
                                updateBudget={this.updateBudget}
                            />
                        )}
                    />

                    <Route
                        exact
                        path="/movies/:id"
                        render={({ match }) => (
                            <Description
                                movie={state.movies[match.params.id]}
                            />
                        )}
                    />
                </div>
            </Router>
        );
    }
}
export default App;
