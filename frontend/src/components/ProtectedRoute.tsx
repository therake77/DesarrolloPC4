import { Navigate } from "react-router"

interface ProtectedRouteProps {
    children : React.ReactNode
};

export default function ProtectedRoute({
    children
} : ProtectedRouteProps ){
    const token = localStorage.getItem("access_token")
    console.log(token)
    if(!token){
        return (<Navigate to="/login" replace/>)
    }

    return (
        <>
            {children}
        </>
    )
}