
import React,{ useState,useEffect } from "react";
import axios from "axios"
import Category from "../category"
import "/Breakdown.css"


function Breakdown() {
    const [breakdown, setBreakdown] = useState([]);
    useEffect(()=>{
        axios.get('http://localhost:8080/categories/breakdown').then(res=>{setBreakdown(res.data)})
    },[])
    return <div className="breakdown">{breakdown.map((c,i)=><Category key={i} category={c}/>)}</div>;
}

export default Breakdown;