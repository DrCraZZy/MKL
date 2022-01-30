import { Route, Routes } from "react-router-dom";

import Hearder from "./layout/Header";
import Footer from "./layout/Footer";

import Registrations from "./pages/registration";

import Home from "./pages/Home";
import CustomerRegistration from "./pages/CustomerRegistration";
import TransporterRegeistration from "./pages/TransporterRegeistration";
import NotFound from "./pages/NotFound";

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
                    <Route element={ <NotFound /> }/>
                </Routes>
            </main>
            <Footer />
        </>
    );
}

export default App;
