import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Transactions from "./components/transactions/Transactions.jsx";
import Operations from "./components/operations/Operations.jsx";
import NavBar from "./components/navbar/Navbar.jsx";
import Breakdown from "./components/breakdown/Breakdown.jsx";
import * as constants from "./constants/consts.js";

function App() {
    return (
        <Router>
            <div className="app-container">
                <NavBar />
                <Route
                    exact path={constants.HOME_PATH}
                    component = {<Transactions/>}
        
                />
                <Route
                    exact path={constants.OPERATIONS_PATH}
                    component={<Operations/>}
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
