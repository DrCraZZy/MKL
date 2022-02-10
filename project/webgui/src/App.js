import { Route, Routes } from "react-router-dom";

import Hearder from "./layout/Header";
import Footer from "./layout/Footer";

import Registrations from "./pages/Registration";

import Home from "./pages/Home";
import CustomerRegistration from "./pages/CustomerRegistration";
import TransporterRegeistration from "./pages/TransporterRegeistration";
import NotFound from "./pages/NotFound";
import Error from "./pages/Error";
import NewCustomer from "./pages/NewCustomer";
import NewTransporter from "./pages/NewTransporter";

function App() {
    return (
        <>
            <Hearder />
            <main className="container content">
                <Routes>
                    <Route exact path="/" element={ <Home /> }/>
                    <Route path="/registration" element={ <Registrations /> }/>
                    <Route path="/customerregistration" element={ <CustomerRegistration />} />
                    <Route path="/transporterregeistration" element={ <TransporterRegeistration />} />
                    <Route path="/error" element={ <Error /> } />
                    <Route path="/newcustomer" element={ <NewCustomer /> } />
                    <Route path="/newtransporter" element={ <NewTransporter /> } />

                    <Route element={ <NotFound /> }/>
                </Routes>
            </main>
            <Footer />
        </>
    );
}

export default App;
