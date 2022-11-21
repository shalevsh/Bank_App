import React from "react";
import "category.css"
import * as constants from "../../constants/consts.js"

function Category(props) {
    const categoryProp = props.category
    return( 
        <div className="category-card">
            <div className="category-text-card">
                {categoryProp ? 
                <>
                <h4 >{categoryProp.category}</h4>
                <h4 >{categoryProp.amount}{constants.COIN_CURRENCY}</h4>
                </>:
                <h1 >{constants.NO_CATEGORY}</h1>
                }
               
            </div>
        </div>
        );
}

export default Category