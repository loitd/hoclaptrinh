// --------------------------------------
// React Native Lesson 04
// youtube.com/tranducloi
// github.com/loitd/hoclaptrinh
// --------------------------------------

// Lessons whole playlist: https://www.youtube.com/watch?v=xp3MqRPfHS8&list=PLzEEDSVPTnyd7cuaPVHFhTUT5oA_v4YyI
// 01: Introduction
// 02: Install & create first application
// 03: Create application main UI 
// 04: Handle input from users
// 05: Loading screens with ActivityIndicator + React Native Networking to pull/fetch information
// 07: Conditional rendering + dynamic background

import React from 'react';
import {View, Text, Image, 
    StyleSheet, TextInput, 
    KeyboardAvoidingView,
    ImageBackground, Platform,
    ActivityIndicator
} from 'react-native';
import SearchInput from '../components/SearchInput';
var {print, getWeatherFromLocation} = require('lutilsjs');

export default class WeatherScreen extends React.Component{
    constructor (props) {
        super(props);
        this.state = {
            location: '',
            // for loading screen
            loading: false,
            error: false,
            the_temp: 0, //temperature
            weather_state_name: '', //description
            weather_state_abbr: 'background',
        };
    }

    componentDidMount(){
        print("Yeah, WeatherScreen mounted!");
        this.handleLocationUpdated('Hà Nội');
    }

    getBackgroundForWeather = (weather_state_abbr) => {
        switch(weather_state_abbr){
            case "c":
                return require("../assets/images/c.jpg");
                break;
            case "h":
                return require("../assets/images/h.jpg");
                break;
            case "hc":
                return require("../assets/images/hc.jpg");
                break;
            case "hr":
                return require("../assets/images/hr.jpg");
                break;
            case "lc":
                return require("../assets/images/lc.jpg");
                break;
            case "lr":
                return require("../assets/images/lr.jpg");
                break;
            case "s":
                return require("../assets/images/s.jpg");
                break;
            case "sl":
                return require("../assets/images/sl.jpg");
                break;
            case "sn":
                return require("../assets/images/sn.jpg");
                break;
        }
    }

    handleLocationUpdated = (newlocation) => {
        this.setState({loading: true}, async () => {
            try{
                if (!newlocation) return;
                // Now getting weather info
                const wea = await getWeatherFromLocation(newlocation);
                if (wea.result){
                    this.setState({
                        loading: false, 
                        error: false, 
                        location: wea.title, 
                        weather_state_name: wea.weather_state_name, 
                        the_temp: wea.the_temp,
                        weather_state_abbr: wea.weather_state_abbr,
                    });
                } else {
                    throw("Update location failed!");
                }
                print("Updated location done!");
            } catch(e){
                this.setState({loading: false, error: true});
            }
        });
    };
    
    // define static methods
    static navigationOptions = {
        header: null,
    };
    
    // begin render
    render() {
        // default location
        const {location, loading, error, weather_state_name, weather_state_abbr, the_temp} = this.state;

        return (
            <KeyboardAvoidingView style={mstyles.container} behavior="padding">       
            {/* <View style={mstyles.container}> */}
                <ImageBackground 
                source={this.getBackgroundForWeather(weather_state_abbr)}
                style={mstyles.imgcontainer}
                imageStyle={mstyles.img}>
                    <View style={mstyles.content}>
                        <ActivityIndicator animating={loading} color="yellow" size="large" />
                        <Text style={[mstyles.h1, mstyles.txt]}>{location}</Text>
                        <Text style={[mstyles.small, mstyles.txt]}>{weather_state_name}</Text>
                        <Text style={[mstyles.h2, mstyles.txt]}>{the_temp}°C</Text>
                        
                        <SearchInput placeholder="Tìm kiếm địa danh"
                        placeholderTextColor="black"
                        onSubmit={this.handleLocationUpdated}/>
                        {/* The way we call image in React Native */}
                        {/* <Image source={require('../assets/images/background.jpg')} style={mstyles.backgroundimg} /> */}

                        {/* Conditional display */}
                        {!loading && (
                            <View>
                                {error && (
                                    <Text style={[mstyles.txt, mstyles.red]}>
                                        City not found. Please choose another location!
                                    </Text>
                                )}
                            </View>
                        )}

                    </View>
                </ImageBackground>
            {/* </View> */}
            </KeyboardAvoidingView>
        );
    }

}

// begin defining styles
const mstyles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#34495E',
        // alignItems: 'center',
        // justifyContent: 'center',
    },
    imgcontainer:{
        flex: 1,
    },
    img:{
        flex: 1,
        width: null,
        height: null,
        resizeMode: 'cover',
    },
    content: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0,0,0,0.275)', //for overlay
    },
    txt: {
        fontFamily: Platform.OS === 'ios' ? 'AvenirNext-Regular' : 'Roboto',
        paddingHorizontal: 10,
        paddingVertical: 10,
    },
    h1: {
        fontSize: 44,
        lineHeight: 50,
        color: 'yellow',
        fontWeight: 'bold',
    },
    h2: {
        fontSize: 38,
        lineHeight: 44,
        color: 'yellow',
    },
    small: {
        fontSize: 18,
        lineHeight: 22,
        color: 'yellow',
    },
    red: {
        color: 'red',
    }
});