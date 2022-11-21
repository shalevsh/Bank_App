import React from "react";
import "transactionItem.css"
import * as constants from "../../../constants/consts.js";


function TransactionItem(props) {
    //what if the transaction is undefined ?
    const transactionClassName = props.transaction.is_deposite ? "positive-text" : "negative-text"
    const transactionAmount =`${props.transaction.amount}${constants.COIN_CURRENCY}`
    return(
            <div className="text-card">
                <h4 className={transactionClassName}>{transactionAmount}</h4>
            </div>
        );
}

export default TransactionItem;