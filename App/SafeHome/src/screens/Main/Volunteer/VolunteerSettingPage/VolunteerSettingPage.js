import React, { Component } from "react";
import { 
    View,
    Text,
    StyleSheet,
    Image,
} from "react-native";
import { createStackNavigator } from 'react-navigation';


class VolunteerSettingPage extends Component {
    render() {
        return (
            <View style={styles.container}>
                <Text>VolunteerSettingPage</Text>
            </View>
        );
    }
}

const VolunteerSettingPageStackNavigation = createStackNavigator({
    VolunteerSettingPage: {
        screen: VolunteerSettingPage,
        navigationOptions: {
            headerLeft: null,
            headerTitle: (
                <Image
                    resizeMode="contain"
                    source={require('../../../../../assets/img/plaingrey-07.png')}
                    style={{ height: 50, width: 50, flex: 1 }} />
            ),
        },
    },
});

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    }
});

export default VolunteerSettingPageStackNavigation;
