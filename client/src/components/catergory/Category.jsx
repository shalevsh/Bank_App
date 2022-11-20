import React from "react";
import "category.css"
import * as constants from "../../constants/consts.js"

function Category(props) {
    return( 
        <div className="category-card">
            <div className="category-text-card">
                <h4 >{props.category.category}</h4>
                <h4 >{props.category.amount}{constants.COIN_CURRENCY}</h4>
            </div>
        </div>
        );
}

export default Category