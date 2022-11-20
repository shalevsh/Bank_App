import React from "react";
import { Link } from "react-router-dom";
import "/navbar.css";
import * as constants from "../../constants/consts.js";
function NavBar() {
        return (
            <div className="navbar-container">
                <Link className="link" to={constants.HOME_PATH}>
                    {constants.TRANSACTIONS}
                </Link>

                <Link
                    className="link"
                    to={constants.OPERATIONS_PATH}>
                    {constants.OPERATIONS}
                </Link>

                <Link
                    className="link"
                    to={constants.BREAKDOWN_PATH}>
                    {constants.BREAKDOWN}
                </Link>
            </div>
        );
    }
export default NavBar;