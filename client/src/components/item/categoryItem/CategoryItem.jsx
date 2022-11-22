import React from "react";
// import "categoryItem.css"
function CategoryItem(props) {

    return(
            <div className="text-card">
               <h4>{props.category.category}</h4>
                <h4>{props.category.vendor}</h4>
            </div>
        );
}
export default CategoryItem;
