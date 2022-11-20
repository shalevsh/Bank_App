import React, { Component } from "react";
import { Link } from "react-router-dom";

import "../styles/navbar.css";
import * as constants from "../constants/consts.js";

class NavBar extends Component {
    handleCatalogClick = (event) =>
        this.props.user === null ? event.preventDefault() : null;

    render() {
        return (
            <div className="navbar-container">
                <Link className="link" to="/">
                    {constants.HOME}
                </Link>

                <Link
                    className="link"
                    to="/catalog"
                    onClick={this.handleCatalogClick}
                >
                    {constants.CATALOG}
                </Link>
            </div>
        );
    }
}

export default NavBar;
