
import React,{ useState,useEffect } from "react";
import axios from 'axios';
import Category from "../catergory/Category.jsx"
// import "/Breakdown.css"
import * as constants from "../../constants/consts.js"


function Breakdown() {
    const [breakdown, setBreakdown] = useState([]);
    useEffect(()=>{
        axios.get(`${constants.BREAKDOWN_URL}`).then(res=>{setBreakdown(res.data)})
    },[])
    return <div className="breakdown">
        {breakdown.map(category=><Category key={category.id} category={category}/>)}
        </div>;
}

export default Breakdown;