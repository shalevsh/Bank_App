import React, { Component } from "react";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Transactions from "./components/transactions/";
import Operations from "./components/operations";
import NavBar from "./components/navBar";
import Breakdown from "./components/breakdown";
import * as constants from "./constants/consts.js";

function App() {
    return (
        <Router>
            <div className="app-container">
                <NavBar />
                <Route
                    path={constants.HOME_PATH}
                    exact
                    render={() => (
                        <Transactions
                            users={state.users}
                            changeUser={this.changeUser}
                        />
                    )}
                />
                <Route
                    path={constants.OPERATIONS_PATH}
                    exact
                    render={() => (
                        <Operations
                            movies={state.movies}
                            toggleRentStatus={this.updateRentStatus}
                            updateBudget={this.updateBudget}
                        />
                    )}
                />

                <Route
                    exact
                    path={constants.BREAKDOWN_PATH}
                    component={<Breakdown />}
                />
            </div>
        </Router>
    );
}
export default App;
