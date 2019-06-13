import React from 'react';
import {View, Text, Image} from 'react-native'

export default class WeatherScreen extends React.Component{
    // define static methods
    static navigationOptions = {
        header: null,
    };
    
    // begin render
    render() {
        return (
            <View style={mstyles.container}>
                <Text style={mstyles.heading1}>
                    This is Loitd from youtube.com/tranducloi
                </Text>
                <Image source={require('../assets/images/background.jpg')} style={mstyles.backgroundimg} />
            </View>
        );
    }

}

// begin defining styles
const mstyles = StyleSheet